from .types import DummyDecimalType, DummyIntegerType
from typing import TypedDict

SystemParameters = TypedDict('SystemParameters', {'DUMMY Length Multiplier': DummyIntegerType})

BehavioralParameters = TypedDict('BehavioralParameters', {'DUMMY D Probability': DummyDecimalType})

FunctionalParameters = TypedDict('FunctionalParameters', {'FP DUMMY Length-2 ABC Combo Boundary Action': str, 'FP DUMMY Length-1 DEF Control Action': str})

Parameters = TypedDict("Parameters",{**BehavioralParameters.__annotations__,
 **FunctionalParameters.__annotations__,
**SystemParameters.__annotations__})

functional_parameters: FunctionalParameters = {"FP DUMMY Length-2 ABC Combo Boundary Action": None,
"FP DUMMY Length-1 DEF Control Action": None,
}

behavioral_parameters: BehavioralParameters = {"DUMMY D Probability": None,
}

system_parameters: SystemParameters = {"DUMMY Length Multiplier": None,
}

parameters: Parameters = {**behavioral_parameters, **functional_parameters, **system_parameters}