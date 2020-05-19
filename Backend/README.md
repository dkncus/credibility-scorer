## How To

### Environment Setup

Remember to run the following command to download all dependencies (Note: Using python 3.7).

```
pip install -r requirements.txt
```

Try to use a conda environment specifically for this project and then whenever you add in a new dependency, use the following command to update the `requirements.txt` file for other devs.

```
pip freeze > requirements.txt
```

### Data Setup

There should be an empty `data` folder. The kaggle dataset here (https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset/data#) was downloaded and the accompanying CSV files are put in there. As such, all pathways are coded to expect this but DO NOT upload the data onto the repo. I've included a gitignore but just a quick reminder.

Also, currently we're trying out glove embeddings so download the pretrained embeddings here (https://nlp.stanford.edu/projects/glove/) and put the glove.6B.300d.txt file in the data folder as well.

### Running the model

The following command allows you to run the full pipeline. That script runs through preprocessing (if necessary files are missing) before running the training process

```
./run_pipeline.sh
```
