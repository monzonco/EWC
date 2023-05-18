bioDes = "Carla Urbanas is a Licensed Professional Clinical Counselor with Supervisory designation and a Licensed Independent Chemical Dependency Counselor. She is certified in EMDR, certified as a Trauma Treatment Specialist, and is a certified Paramedic in Ohio. She specializes in working with Police, Fire, and Military Personnel, critical incident stress debriefings and trauma.\n" 
bioDes2 = " With 22 years of experience as a counselor and almost 30 years of experience in the mental health field, she enjoys being a clinician in her private practice working with a broad spectrum of clients.\n"  
bioDes3 = " Other areas of expertise are substance abuse/dependence, codependency, depression, anxiety, grief/loss, marital issues, family issues, and other mood disorders\n"
bioDes4 = " In addition to being a prominent therapist, Carla is the owner/practice manager of Professional Counseling Services of Ohio, LLC. She currently sits on the board of directors of The Association of Traumatic Stress Specialists. She is the clinical consultant for several local peer support teams and she regularly presents on topics such as EMDR, CISM, and peer support.\n"
bioDes5 = " She has also presented on topics such as working with public safety, military related issues, stress management, substance use issues, grief/loss issues, ADHD and mood disorders.\n"
bioDes6 = " Carla Urbanas takes an interactive, solution focused approach. Her therapeutic approach is to provide support and practical feedback to help her clients effectively address personal life challenges. She also utilizes EMDR regularly with her clients as needed and desired by her clients. With compassion and understanding, she works with each individual to help them build on their strengths and attain the personal growth they are committed to accomplishing.\n"
bioDes = bioDes + bioDes2 + bioDes3 + bioDes4 + bioDes5 + bioDes6
listDes = bioDes.split("\n")
for  i in listDes:
    if len(i) > 0:
     print('<strong>'+i+ '</strong>\n')
#print(bioDes)
print(len(bioDes))