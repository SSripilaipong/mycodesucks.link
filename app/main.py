from lambler import Lambler
from lambler.content import LocalFile

import endpoint

lambler = Lambler()

lambler.handle(endpoint.handler)

lambler.use_content(LocalFile())
