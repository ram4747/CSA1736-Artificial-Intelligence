symptom(fever, [flu, cold, malaria]).
symptom(cough, [flu, cold]).
symptom(headache, [flu, migraine]).
symptom(rash, [allergy, measles]).
symptom(runny_nose, [flu, cold]).
symptom(fatigue, [flu, malaria]).
symptom(sneezing, [cold, allergy]).
symptom(chills, [malaria, flu]).
diagnose(Disease, Symptoms) :-
    symptom(Symptom, Diseases),
    member(Symptom, Symptoms),
    member(Disease, Diseases).
diagnose(Disease, Symptoms) :-
    symptom(Symptom, Diseases),
    member(Symptom, Symptoms),
    member(Disease, Diseases).
