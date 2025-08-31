from datasets import load_dataset
import pandas as pd
import re



def f_dataset_download(dataSetName = "warrenm/movie-dialogues"):
    

    # cleanedNamed = dataSetName.encode("ascii", "ignore").decode()
    cleanedNamed = re.sub(r'[^A-Za-z0-9 ]+', '', dataSetName)  # keep only letters, numbers, and spaces
    excellName = cleanedNamed + ' ' + "___movie_dialogues_train.xlsx"
    jsonName = cleanedNamed + ' ' + "movie_dialogues_train.json"

    # Load dataset
    dataset = load_dataset(dataSetName)

    # Convert one split (e.g., train) into pandas DataFrame
    df = pd.DataFrame(dataset["train"])

    # Save to Excel
    df.to_excel(excellName, index=False)

    # Save to JSON (pretty formatted)
    df.to_json(jsonName, orient="records", lines=False, indent=4)

    print("Dataset saved as Excel and JSON")
    return 0 


def f_dataset_List_download(dataSetList = [  'warrenm/movie-dialogues' 
                                            ,'fka/awesome-chatgpt-prompts'
                                            ,'mylesmharrison/cornell-movie-dialog'
                                            ,'cornell-movie-dialog/cornell_movie_dialog'
                                            ,'spawn99/CornellMovieDialogCorpus'
                                            ,'google/Synthetic-Persona-Chat'
                                            ,'bavard/personachat_truecased'
                                            ,'AlekseyKorshuk/persona-chat'
                                            ,'racineai/OGC_Energy_Arabic'
                                            ,'silma-ai/arabic-broad-benchmark'
                                            ,'bitext/Bitext-customer-support-llm-chatbot-training-dataset'
                                            ,'Victorano/Bitext-customer-support-llm-chatbot-testing-dataset-seed42-4k-4.5k'
                                            ,'Tobi-Bueck/customer-support-tickets'
                                            ,'Kaludi/Customer-Support-Responses'
                                            ,'warabimoti/pop_entertainment'
                                            ,'JYouthCultureQA/POP_entertainment'
                                            ,'DeepNLP/ai-agent-entertainment'
                                            ,'DataDump1/entertainment_reddit'   
                                            ]):

    for dataSetIter in dataSetList :
        try:
            print('*'*100)
            print('*'*100)
            print(dataSetIter)
            print('*'*100)
            print('*'*100)
            f_dataset_download(dataSetName = dataSetIter)
        except:
            print("Something wrong with " + dataSetIter)
    return 0





# f_dataset_List_download()

