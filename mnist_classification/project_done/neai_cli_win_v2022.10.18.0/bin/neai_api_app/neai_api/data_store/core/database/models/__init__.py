from .library_model import Library
from .optimization_model import Optimization, OptimizationSignalAssociation
from .progression_model import Progression
from .project_model import Project
from .result_model import Result
from .signal_model import Signal


# ---
# Tools
def update_model(model, update_dict):
    """Update a model based on a dictionnary"""

    for key, value in update_dict.items():
        # Update field
        update_field = getattr(model, "update_field", None)
        if callable(update_field):
            update_field(key, value)
        else:
            setattr(model, key, value)
    return model


def get_column_type(column):

    try:
        return str(column.type)
    except:
        return 'Json'
