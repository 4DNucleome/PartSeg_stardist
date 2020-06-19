from .stardist_plugin import StardistSegmentation

def register():
    print("buka")
    from PartSegCore.register import register, RegisterEnum

    register(StardistSegmentation, RegisterEnum.mask_algorithm)
