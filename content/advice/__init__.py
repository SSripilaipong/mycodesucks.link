from ._base import Advice, Paragraph, Video
from ._break_monolith_into_modules import break_monolith_into_modules
from ._separate_layers_with_clean import separate_layers_with_clean
from ._testcase_before_refactor import testcase_before_refactor
from ._too_much_coupling import too_much_coupling

advice_mapper = {advice.id_: advice for advice in [
    too_much_coupling,
    break_monolith_into_modules,
    separate_layers_with_clean,
    testcase_before_refactor,
]}
