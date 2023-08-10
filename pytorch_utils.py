import torch
import torch.nn.functional as F

def patch_img(img, k=8):      # (bs, C, H, W)
    bs, C, H, W = img.shape
    x = F.unfold(img, kernel_size=k, stride=k)    # (bs, C*k*k, L), C是通道数, L是每个通道能分成的块数量
    x = x.view(bs, C, k, k, -1)       # (bs, C, k, k, L)
    x = x.permute(0, 4, 1, 2, 3)     # (bs, num_patch, C, k, k)

    return x

x = torch.rand(10, 3, 256, 256)
y = patch_img(x, 8)
print(y.shape)        # (10, 1024, 3, 8, 8)
