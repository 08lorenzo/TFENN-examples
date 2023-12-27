# Copyright 2023 Kévin Garanger
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Callable

from jax import numpy as jnp
from TFENN.util.enum_input import EnumInputFun


class LossType(EnumInputFun):
    SE = "se"
    NSE = "nse"

    @classmethod
    @property
    def fun_map(cls) -> dict["LossType", Callable[[jnp.ndarray, jnp.ndarray], float]]:
        return {
            LossType.SE: lambda y_true, y_pred: ((y_true - y_pred) ** 2).sum(),
            LossType.NSE: lambda y_true, y_pred: ((y_true - y_pred) ** 2).sum()
            / jnp.clip((y_true**2).sum(), a_min=1e-3),
        }
