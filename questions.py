from mcq import Questions

print("your mcq questions will be given below!!:")
prompt=["1.who is father of our nation:\na.gandhi,\nb.nehru,\nc.modi",
        "2.which state iis called as gateway of india:\na.delhi,\nb.mumbai,\nc.chennai",
        "3.who wrote our Inian National Anthem:\na.tagore\nb.patel\nc.sivaji",
        "4.How many districts in TamilNadu:\na.32\nb.35\nc.38"]
test=[Questions(prompt[0],answer="a"),Questions(prompt[1],answer="b"),Questions(prompt[2],answer="a"),Questions(prompt[3],answer="c")]
def run_test():
    marks=0
    for question in test:
        print(question.question)
        ans=input("enter your choice :")
        if ans==question.answer:
            marks+=1

        print(f"your marks {marks}/{len(test)}")
run_test()
print("Test completed!!")
