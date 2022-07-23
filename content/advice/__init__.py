from ._base import Advice, Paragraph, Video
from ._break_monolith_into_modules import break_monolith_into_modules
from ._too_much_coupling import too_much_coupling

advice_mapper = {
    too_much_coupling.id_: too_much_coupling,
    break_monolith_into_modules.id_: break_monolith_into_modules,
}
