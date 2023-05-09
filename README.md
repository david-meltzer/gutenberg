# Visualizing Literature using Transformers

This repository is a work-in-progress on visualizing and comparing works of literature using transformer models.
The novels are scraped from <a href="https://www.gutenberg.org/">Project Gutenberg<a> using BeautifulSoup, see the code in the gutenberg_scraper.py file. 
At the moment I have analyzed the following works by James Joyce, "Dubliners", "A Portrait of the Artist as a Young Man", and "Ulysses" as well as three translation of "The Odyssey" by Homer. In I looked at the translations done by Alexander Pope (1725), Butcher and Lang (1879), and Samuel Butler (1897) since these are all in the public domain.
  
To visualize the data, I first used <a href="https://www.sbert.net/">SentenceTransformers</a> to embed spans of text into high-dimensional vector spaces which effectively capture the semantic meaning of the text. The data can then be visualized using dimensional reduction techniques such as UMAP and T-SNE. It is also possible to measure the effective distances between different chapters of a given book using this high-dimensional vector space and the distances can be visualized using heatmaps.
  
For a more thorough discussion of these models and the books we are studying, please see the following Weights and Biases <a href="https://wandb.ai/dmeltzer/gutenberg/reports/Visualizing-Literature-using-Transformers--Vmlldzo0MTIyODEx?accessToken=1ekch7p12170nvwbtqzvy2g3shpyyboajfbalciun3ly913cdv033je1rvkoa5bj">report</a>.
