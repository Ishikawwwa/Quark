import ollama

all_skills = []

def rec_build(skill_name, area):
    response = ollama.chat(model='llama3.1', messages=[
    {
        'role': 'system',
        'content': "You are a system used to describe the following tree graph structure: Let's imagine that all the scientific domain knowledge is represented in terms of practical skills. All of these skills can be considered as a particular lesson, so a person has to complete all the subskill lessons to learn the skill they want to. Answer with a plain explanation to the primary skill(skills that are known for a school student(like counting, reading, basic human functions, etc.). Answer with a list of sub-skills otherwise."
    },
    {
        'role': 'user',
        'content': f"Would {skill_name} skill ({area}) be primary or complex(those skills are harder then a high school level) and made of subskills? If it is primary, respond with a clear explanation, otherwise respond only with the names of the sub-skills as a list(each skill on a separate line starting with '!' symbol), nothing else, no justifications. Do not break skills into abstract ones, only pure technical skills that can have a distinct lesson in a university or school. Do not leave the domain of practical skills of {area}. For example, if input skill is Basic Algebra or Arithmetics, then the output must be: Primary skill. Another example, if input skill is Linear Algebra, then the list of subskills is shown.",
    },
    ])
    
    if "primary" in response['message']['content'].lower():
        return

    print(f"Sub-skills for {skill_name}:")
    print(response['message']['content'])
    print()
    
    results = response['message']['content'].split('\n')

    results_filtered = []
    for i in range(len(results)):
        if '.' not in results[i] and '!' not in results[i]:
            continue
        if '.' in results[i]:
            if results[i].split('.')[1].strip():
                results_filtered.append(results[i].split('.')[1].strip())
        else:
            if results[i].split('!')[1].strip():
                results_filtered.append(results[i].split('!')[1].strip())

    print(results_filtered)

    for res in results_filtered:
        if res not in all_skills:
            all_skills.append(res)
            rec_build(res, area)


rec_build("Calculus", "Mathematics")