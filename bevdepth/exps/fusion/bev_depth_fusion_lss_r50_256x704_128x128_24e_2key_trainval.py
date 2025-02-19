# Copyright (c) Megvii Inc. All rights reserved.
from bevdepth.exps.base_cli import run_cli
from bevdepth.exps.fusion.bev_depth_fusion_lss_r50_256x704_128x128_24e_2key import \
    BEVDepthLightningModel as BaseBEVDepthLightningModel  # noqa


class BEVDepthLightningModel(BaseBEVDepthLightningModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.train_info_paths = [
            'data/nuScenes/nuscenes_infos_train.pkl',
            'data/nuScenes/nuscenes_infos_val.pkl'
        ]


if __name__ == '__main__':
    run_cli(BEVDepthLightningModel,
            'bev_depth_fusion_lss_r50_256x704_128x128_24e_2key_trainval')
