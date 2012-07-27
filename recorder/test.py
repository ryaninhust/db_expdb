
from context import Context
from context import context


def test1(f):
    def w(*args,**kwargs):
        a= f(*args,**kwargs)
        return a
    return w

@context.func_collector
def test2(a,b):
    print "asd"
    return 1

@context.func_collector
def test1(a,b):
    return test2(a=a,b=b)



@context.func_collector
def sofia_ml(dimensionality, _lambda, iterations, learner_type, loop_type, random_seed, rank_step_probability, model_out, training_file):
#os.system("...")
    pass

if __name__=="__main__":
    sofia_ml(dimensionality=65, _lambda=0.3, iterations=3000, learner_type='least-mean-squares', loop_type='combined-ranking', random_seed=5, rank_step_probability=1,model_out='/path/to/outfile', training_file='/path/to/training_file')
    context.save()
    print context.find_one()
    
    
    

    

