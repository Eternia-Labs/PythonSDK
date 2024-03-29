SERVICE_ID = "SCPartnersSolutions"

# region Desired Ops
OP_ADD_SOLUTION_TO_PROPERTY = "addSolutionToProperty"
OP_GET_SOLUTION_FOR_PROPERTY = "getSolutionForProperty"
OP_LIST_ALL_SOLUTIONS_FOR_PROPERTY = "listAllSolutionsForProperty"
OP_APPROVE_SOLUTION_FOR_PROPERTY = "approveSolutionForProperty"
OP_DENY_SOLUTION_FOR_PROPERTY = "denySolutionForProperty"

OPS = {
    OP_ADD_SOLUTION_TO_PROPERTY,
    OP_GET_SOLUTION_FOR_PROPERTY,
    OP_LIST_ALL_SOLUTIONS_FOR_PROPERTY,
    OP_APPROVE_SOLUTION_FOR_PROPERTY,
    OP_DENY_SOLUTION_FOR_PROPERTY,
}
# endregion

RESPONSE_DATA_TEMPLATE = {"code": None, "data": None, "message": "default"}
