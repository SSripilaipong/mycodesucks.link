from ._base import Advice, Paragraph, Video
from ._break_monolith_into_modules import break_monolith_into_modules
from ._ddd_for_communication import ddd_for_communication
from ._event_storming_for_unity import event_storming_for_unity
from ._refactor_should_use_ddd import refactor_should_use_ddd
from ._separate_layers_with_clean import separate_layers_with_clean
from ._testcase_before_refactor import testcase_before_refactor
from ._too_much_coupling import too_much_coupling

advice_mapper = {advice.id_: advice for advice in [
    too_much_coupling,
    break_monolith_into_modules,
    separate_layers_with_clean,
    testcase_before_refactor,
    refactor_should_use_ddd,
    ddd_for_communication,
    event_storming_for_unity,
]}
