from pathlib import Path


class PTSIndexer:
    pass


class IntIndexer:
    pass


class Reader:
    def __init__(self, path: Path):
        raise NotImplementedError

    @property
    def by_pts(self) -> PTSIndexer:
        raise NotImplementedError

    @property
    def by_idx(self) -> IntIndexer:
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __getitem__(self, idx):
        raise NotImplementedError
