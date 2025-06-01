import arcade


def load_animation(folder) -> dict[str, list[arcade.Texture]]:
    frames = sorted(folder.glob("*.png"))
    original = [arcade.load_texture(str(f)) for f in frames]
    flipped = [arcade.load_texture(str(f), mirrored=True) for f in frames]
    return {"right": original, "left": flipped}
