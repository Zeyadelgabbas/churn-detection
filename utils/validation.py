from pydantic import BaseModel, Field
from typing import Literal


class CustomerData(BaseModel):
    CreditScore: int = Field(..., ge=0, description="Credit score must be >= 0")
    Geography: Literal["Germany", "France", "Spain"] = Field(..., description="Only Germany, France, or Spain")
    Gender: Literal["Male", "Female"] = Field(..., description="Only Male or Female")
    Age: int = Field(..., ge=18, le=100, description="Age must be between 18 and 100")
    Tenure: int = Field(..., ge=0, le=10, description="Tenure must be between 0 and 10")
    Balance: float = Field(..., ge=0, description="Balance must be >= 0")
    NumOfProducts: int = Field(..., ge=1, le=4, description="Number of products must be between 1 and 4")
    HasCrCard: Literal[0, 1] = Field(..., description="Has credit card: 0 or 1")
    IsActiveMember: Literal[0, 1] = Field(..., description="Is active member: 0 or 1")
    EstimatedSalary: float = Field(..., ge=0, description="Estimated salary must be >= 0")

    pass