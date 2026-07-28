import argparse
from pathlib import Path

from PIL import Image


def main():
    parser = argparse.ArgumentParser(
        description="Cut a ten-screen ecommerce detail master into equal lossless PNG slices."
    )
    parser.add_argument("master", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--screens", type=int, default=10)
    parser.add_argument("--prefix", default="detail")
    args = parser.parse_args()

    if args.screens < 1:
        raise ValueError("--screens must be positive")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    with Image.open(args.master) as master:
        image = master.convert("RGB")
        width, height = image.size
        if height % args.screens:
            raise ValueError(
                f"Master height {height} is not divisible by {args.screens}"
            )
        screen_height = height // args.screens
        for index in range(args.screens):
            top = index * screen_height
            slice_image = image.crop((0, top, width, top + screen_height))
            output = args.output_dir / f"{args.prefix}-{index + 1:02d}.png"
            slice_image.save(output, "PNG", optimize=True)

    print(
        f"Created {args.screens} slices of {width}x{screen_height} "
        f"from {args.master}"
    )


if __name__ == "__main__":
    main()
