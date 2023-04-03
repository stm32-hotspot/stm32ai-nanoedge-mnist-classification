from .build_buffers import BuildBufferFormatterTask
from .extract_cols import ExtractColsFormatterTask
from .extract_lines import ExtractLinesFormatterTask
from .downsample import DownsampleFormatterTask
from .get_info import GetInfoFormatterTask
from .reformat import ReformatFormatterTask
from .remove_lines import RemoveLinesFormatterTask
from .shuffle import ShuffleFormatterTask
from .split import SplitFormatterTask

FORMATTER_TASKS_CLS = [
    BuildBufferFormatterTask,
    ExtractColsFormatterTask,
    ExtractLinesFormatterTask,
    DownsampleFormatterTask,
    GetInfoFormatterTask,
    ReformatFormatterTask,
    RemoveLinesFormatterTask,
    ShuffleFormatterTask,
    SplitFormatterTask
]
