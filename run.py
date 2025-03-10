from NLU_module import NLU

nlu_module = NLU()
for _ in range(4):
    user_input = input('Input: \n')
    response = nlu_module.run(user_input=user_input)
    print(response)