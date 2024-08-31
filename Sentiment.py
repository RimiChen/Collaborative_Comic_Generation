### import libraries
from transformers import pipeline
from transformers import Conversation
import json
from sentence_transformers import SentenceTransformer
import numpy as np
import scipy
from sklearn import preprocessing
# import numpy as np
# import torchvision
# from torchvision import transforms
# import torch.nn.functional as nn
# import torch


class Sentiment():


    # the smallest k diatances
    # compute sentiment score
    def __init__(self, model_name):
        self.model_name = model_name
        self.test_words = "retrieve labels"
        self.prefix_sentence = "I "
        self.postfix_sentence = "."

        self.classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

        label_retrieving = self.classifier(self.test_words)
        self.sentiment_labels = []
        
        ### get the sentiment list
        # list of dictionary
        self.exclude_list = [
            "neutral"
            ] 

        for labels in label_retrieving:
            for label in labels:
                if label["label"] not in self.sentiment_labels:
                    if label["label"] not in self.exclude_list:
                        self.sentiment_labels.append(label["label"])

        ### using SBERT to transform the words into vectors
        # Load pre-trained SBERT model
        self.sentence2Vec_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

        self.emotion_score = self.PAD_emotion_state_model()

        emotion_score_vector = [self.emotion_score[emotion]["value"] for emotion in self.emotion_score.keys()]
        emotion_score_vector = np.array(emotion_score_vector)
        # print(emotion_score_vector)
        # print(type(emotion_score_vector))        
        # print(json.dumps(self.emotion_score, sort_keys=True, indent=4))
        


        ### TODO: compute the distance matrix in more matrix way to speed up        
       
        ### the distance between sentiment label and emotions in PAD emtion state model
        self.sentiment_label_distance = {}

        for sentiment in self.sentiment_labels:
            # get embedding
            embedding = self.generateEmbeddings(sentiment)
            # embedding = embedding.reshape(-1, 1)
            # print(embedding.shape)
            # print(sentiment)

            distance_mat = []
            for emotion in self.emotion_score.keys():
                # print(emotion)
                distance = self.getDistance(self.emotion_score[emotion]["vector"], embedding)
                distance_mat.append(distance)

            # distance_mat = [self.getDistance(self.emotion_score[emotion]["vector"], embedding) for emotion in self.emotion_score.keys()]
            # print(len(distance_mat))
            # print(distance_mat)
        
            if sentiment not in self.sentiment_label_distance:
                ### normalize the distance
                # tensor = torch.torch.FloatTensor(distance_mat)
                # normalized = nn.normalize(tensor)

                # <class 'numpy.ndarray'>
                # distance = self.toTensorAndNormalize(distance_mat, 0.9)
                distance = np.array(distance_mat)
                
                # distance = self.leftMin2(distance)
                
                # a * (a >= np.sort(a, axis=0)[[-n_max],:]).astype(int)
                
                # print(distance)
                # ratio = (np.ones(distance.shape) - distance)/np.sum(distance)
                # ratio = (np.ones(distance.shape)*np.max(distance) - distance)
                ratio = (np.ones(distance.shape)*np.max(distance) - distance)
                # ratio = self.leftMax2(ratio)
                # print(ratio)

                score = emotion_score_vector * ratio
                # print(score)

                self.sentiment_label_distance[sentiment] = np.sum(score)
                # print(type(distance_mat))
                # print(self.santiment_label_distance[santiment])
                # print(type(self.santiment_label_distance[santiment]))

            
        self.sentiment_label_distance = dict(sorted(self.sentiment_label_distance.items()))
        # print(self.santiment_label_distance)

        sentiment_score_vector = [self.sentiment_label_distance[sentiment] for sentiment in self.sentiment_label_distance.keys()]
        normalized_sentiment_vector = self.toTensorAndNormalize(sentiment_score_vector, 2, -1)
        # scaled_santiment_vector = ((normalized_santiment_vector - normalized_santiment_vector.min()) * (1/(normalized_santiment_vector.max() - normalized_santiment_vector.min()) * 2)).astype('uint8')
        # print(normalized_santiment_vector )


        ### Arousal score for santiment
        self.sentiment_arousal_level = {}
        sentiment_index = 0
        for sentiment in self.sentiment_label_distance.keys():
            if sentiment not in self.sentiment_arousal_level:
                self.sentiment_arousal_level[sentiment] = {}
                self.sentiment_arousal_level[sentiment]["level"] = normalized_sentiment_vector[sentiment_index]
                self.sentiment_arousal_level[sentiment]["index"] = sentiment_index
                sentiment_index = sentiment_index + 1
                # santiment_arousal_level[santiment]["embedding"] = self.generateEmbeddings(santiment)

        print(self.sentiment_arousal_level)
    def getNarrativeIntensity_VANDER(self, input):
        print("Using VADER to get compund score from -1 (most extreme negative) to 1 (most extreme positive).")

    def getNarrativeIntensity_TextBlob_polarity(self, input):
        print("Using TextBlob to get Polarity: -1 to 1 indicating negative to positive")
    
    def getNarrativeIntensity_TextBlob_subjectivity(self, input):
        print("Using TextBlob to get subjectivity score, incating how subjective or objective the text is.")
    
    def getNarrativeIntensity_SentiStrength(self, input):
        print("Using SentiStrength to get score, that is the probability distribution over sentiment classes, interpreted as sentiment intensity scores.")
    

    ### return arousal score 
    def getNarrativeArousalScore(self, input):
        score = 0
        sentiment_prob = self.getSentiments(input)
        
        temp_sentiment_dictionary = {}

        for labels in sentiment_prob:
            for label in labels:
                if label["label"] not in temp_sentiment_dictionary:
                    if label["label"] not in self.exclude_list:
                        self.sentiment_labels.append(label["label"])                    
                        # print(label["label"])
                        # temp_santiment_dictionary[label["label"]] = self.generateEmbeddings(label["label"])
                        temp_sentiment_dictionary[label["label"]] = label["score"]

        temp_sentiment_dictionary = dict(sorted(temp_sentiment_dictionary.items()))
        sentiment_weight = [temp_sentiment_dictionary[sentiment] for sentiment in temp_sentiment_dictionary.keys()]

        # already sorted
        # self.santiment_arousal_level
        sentiment_level = [self.sentiment_arousal_level[sentiment]["level"] for sentiment in self.sentiment_arousal_level.keys()]
        # array_weight = self.toTensorAndNormalize(santiment_weight, 1, 0)
        array_weight = np.array(sentiment_weight)
        array_weight = self.leftMax2(array_weight, 2)
        array_weight = array_weight/ np.sum(array_weight)

        array_level = np.array(sentiment_level)

        score = np.sum(array_weight * array_level)


        print(json.dumps(temp_sentiment_dictionary, sort_keys=True, indent=4))    
        print(array_weight)
        print(array_level)
        print(score)

        return score


    ### getting the sentiments score 
    def getSentiments(self, input_sentence):
        target_sentence = self.prefix_sentence + input_sentence + self.postfix_sentence
        result = self.classifier(target_sentence)

        return result
    
    ### Using SBERT to get sentence vector
    def generateEmbeddings(self, input_sentence):
        embedding  = self.sentence2Vec_model.encode(input_sentence)

        # <class 'numpy.ndarray'>
        return embedding
    
    ### Compute the arousal-nonarousal in PAD emotional state model, assessing the intensity or activation level of an emotion 
    def PAD_emotion_state_model(self):
        # High arousal 1:  Excitement, Anger, Surprise, Astonishment, Thrill
        # Medium arousal 0: Interest, Curiosity, Contentment, Calmness, Relaxation
        # Low arousal -1: Sadness, Boredom, Serenity, Peacefulness, Satisfaction, Loneliness, Dissatisfaction

        high_arousal = {}
        medium_arousal = {}
        low_arousal = {}

        high_arousal["Excitement"] = "high"
        high_arousal["Anger"] = "high"
        high_arousal["Surprise"] = "high"
        high_arousal["Astonishment"] = "high"
        high_arousal["Thrill"] = "high"

        medium_arousal["Interest"] = "medium"
        medium_arousal["Curiosity"] = "medium"
        medium_arousal["Contentment"] = "medium"
        medium_arousal["Calmness"] = "medium"
        medium_arousal["Relaxation"] = "medium"

        low_arousal["Sadness"] = "low"
        low_arousal["Boredom"] = "low"
        low_arousal["Serenity"] = "low"
        low_arousal["Peacefulness"] = "low"
        low_arousal["Satisfaction"] = "low"
        low_arousal["Loneliness"] = "low"  
        low_arousal["Dissatisfaction"] = "low"

        emotion_state_model = {}
        # print(type(emotion_state_model))

        emotion_state_model = self.marge_dictionary(emotion_state_model, high_arousal)
        emotion_state_model = self.marge_dictionary(emotion_state_model, medium_arousal)
        emotion_state_model = self.marge_dictionary(emotion_state_model, low_arousal)

        # print(json.dumps(emotion_state_model, sort_keys=True, indent=4))

        emotion_score = {}
        ### assign scores
        index = 0

        # make the index mapping to each emotion
        sorted_emotion_state_model = dict(sorted(emotion_state_model.items()))

        for emotion in sorted_emotion_state_model.keys():
            # print(emotion)
            if emotion not in emotion_score:
                if emotion_state_model[emotion] == "high":
                    emotion_score[emotion] = {}
                    emotion_score[emotion]["value"] = 1
                    emotion_score[emotion]["vector"] = self.generateEmbeddings(emotion)
                    emotion_score[emotion]["index"] = index
                    index = index + 1


                elif  emotion_state_model[emotion] == "medium":
                    emotion_score[emotion] = {}
                    emotion_score[emotion]["value"] = 0
                    emotion_score[emotion]["vector"] = self.generateEmbeddings(emotion)
                    emotion_score[emotion]["index"] = index
                    index = index + 1

                
                elif emotion_state_model[emotion] == "low":
                    emotion_score[emotion] = {}
                    emotion_score[emotion]["value"] = -1
                    emotion_score[emotion]["vector"] = self.generateEmbeddings(emotion)
                    emotion_score[emotion]["index"] = index
                    index = index + 1
        
        return emotion_score



    ### merge dictionary
    def marge_dictionary(self, dict1, dict2):
        result = {**dict1, **dict2}
        return result  

    def getDistance(self, point1, point2):
        # dist = scipy.spatial.distance.cdist(mat,point)
        # https://stackoverflow.com/questions/1401712/how-can-the-euclidean-distance-be-calculated-with-numpy
        dist = np.linalg.norm(point1-point2)
        
        return dist   
    def toTensorAndNormalize(self, float_list, normalized_coefficent, normalized_shift):
        array = np.array(float_list)
        # normalized = preprocessing.normalize([array])
        normalized = ((array-np.min(array))/(np.max(array)-np.min(array))) * normalized_coefficent +normalized_shift

        return normalized
    
    def leftMax2(self, input_array, kth):
        out = np.zeros_like(input_array)
        # idx  = distance.argmax()
        idx = np.argpartition(input_array, -kth)[-kth:]
        out.flat[idx] = input_array.flat[idx]

        return out  

    ### define test
    def testMethod(self):
        print('Import: ', self.model_name)
        print("Testing the Sentiment distance")
        testing_sentence = "This is an interesting comic generator!"
        arousal_score = self.getNarrativeArousalScore(testing_sentence)
        print("For testing sentence, the arousal level score is : ", arousal_score)



# ### Main starting point
# if __name__ == "__main__":
#     print("Testing the Sentiment distance")
    
#     testing_sentence = "hit"

#     sentiment_scorer = SentimentDistance()
#     # result = santiment_scorer.getSantiments(testing_sentence)
#     arousal_score = sentiment_scorer.getNarrativeArousalScore(testing_sentence)
#     print("Arousal score for \" ", testing_sentence, " \" = ", arousal_score)

#     # print(json.dumps(result, sort_keys=True, indent=4))

#     testing_sentence_vector = "I'm happy."
#     vector = sentiment_scorer.generateEmbeddings(testing_sentence_vector)


