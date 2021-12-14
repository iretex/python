import step1 as s1

# define the stages of the pipeline
pipeline = s1.Pipeline(steps= [('tfidf', s1.TfidfVectorizer(lowercase=True,
                                                      max_features=1000,
                                                      stop_words= s1.ENGLISH_STOP_WORDS)),
                            ('model', s1.LogisticRegression())])

# fit the pipeline model with the training data                            
pipeline.fit(s1.train.tweet, s1.train.label)

# sample tweet
text = ["Virat Kohli, AB de Villiers set to auction their 'Green Day' kits from 2016 IPL match to raise funds"]

# predict the label using the pipeline
pipeline.predict(text)
## >> array([0])

# import joblib
from joblib import dump

# dump the pipeline model
dump(pipeline, filename="model/text_classification.joblib")