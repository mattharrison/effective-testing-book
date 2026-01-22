from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path
from typing import Sequence

import tinylm


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tinylm")
    subparsers = parser.add_subparsers(dest="command", required=True)

    predict_parser = subparsers.add_parser("predict", help="Predict the next token")
    predict_parser.add_argument("--training", help="Training text")
    predict_parser.add_argument("--training-file", type=Path, help="Read training text from a file")
    predict_parser.add_argument("--size", type=int, default=1, help="Model size")
    predict_parser.add_argument("--prefix", required=True, help="Context to predict from")
    predict_parser.add_argument("--seed", type=int, help="Random seed for deterministic runs")

    generate_parser = subparsers.add_parser("generate", help="Generate text from a starting prefix")
    generate_parser.add_argument("--training", help="Training text")
    generate_parser.add_argument("--training-file", type=Path, help="Read training text from a file")
    generate_parser.add_argument("--size", type=int, default=1, help="Model size")
    generate_parser.add_argument("--start", required=True, help="Starting context")
    generate_parser.add_argument("--count", type=int, default=1, help="How many tokens to generate")
    generate_parser.add_argument("--seed", type=int, help="Random seed for deterministic runs")

    return parser


def _load_training_text(args: argparse.Namespace) -> str:
    if args.training is not None and args.training_file is not None:
        raise ValueError("use only one of --training and --training-file")
    if args.training is not None:
        return args.training
    if args.training_file is not None:
        return args.training_file.read_text(encoding="utf-8")
    raise ValueError("training text is required (use --training or --training-file)")


def main2(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    try:
        training = _load_training_text(args)
        if args.seed is not None:
            random.seed(args.seed)

        if args.command == "predict":
            model = tinylm.Markov(training, size=args.size)
            print(model.predict(args.prefix))
            return 0

        if args.command == "generate":
            if args.count < 0:
                raise ValueError("--count must be >= 0")

            model = tinylm.Markov(training, size=args.size)
            out = [args.start]
            context = args.start
            for _ in range(args.count):
                next_token = model.predict(context)
                out.append(next_token)
                context = (context + next_token)[-args.size :]

            print("".join(out))
            return 0

        raise ValueError(f"unknown command: {args.command}")
    except (ValueError, KeyError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.seed is not None:
        random.seed(args.seed)

    try:
        training = _load_training_text(args)
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if args.command == "predict":
        model = tinylm.Markov(training, size=args.size)
        try:
            print(model.predict(args.prefix))
        except (ValueError, KeyError) as exc:
            print(str(exc), file=sys.stderr)
            return 2
        return 0

    if args.command == "generate":
        if args.count < 0:
            print("--count must be >= 0", file=sys.stderr)
            return 2
        model = tinylm.Markov(training, size=args.size)
        out = [args.start]
        context = args.start
        for _ in range(args.count):
            try:
                next_token = model.predict(context)
            except (ValueError, KeyError) as exc:
                print(str(exc), file=sys.stderr)
                return 2
            out.append(next_token)
            context = (context + next_token)[-args.size:]
        print("".join(out))
        return 0

    print(f"unknown command: {args.command}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

