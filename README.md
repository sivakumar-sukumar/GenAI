# GenAI

This is a chatbot to retreive information about documents on Wildlife and Biodiversity in India.


**Tech Stack Recommendations:**

| Layer | Tech Stack |
| --- | --- |
| Frontend (UI) | Cisco Webex Bot API, Adaptive Cards |
| User Interaction Layer | FastAPI, Flask, Webex Webhooks |
| Data Acquisition Layer | BeautifulSoup, Scrapy, Playwright, Semantic Scholar API, CORE API  |
| Data Processing Laye | NLP Libraries (spaCy, NLTK), LangChain, Pinecone/Weaviate/FAISS |
| GenAI Model Layer | OpenAI GPT, Llama |
| Data Presentation Layer | Markdown Formatting, Adaptive Cards |


Without Frontend backend.py can be run from CLI
With webex Frontend frontend.py to be run which calls the backend AI_Mongo.py

Sample Output:

<ins> Question: </ins> <br> <br>
I want to know the publication by Mr. Shivakumar only?

<ins> Answer: </ins> <br> <br>
There are two publications by Mr. Shivakumar:

1. Charting risk pathways of leopard attacks on people: A decision tree approach. Human Dimensions (2025)
2. Examining leopard attacks: spatio-temporal clustering of human-leopard conflicts in the Western Ghats, India. (2023)

<ins> Question: </ins> <br> <br>
what the issues and threats to Wildlife Conservation india?

<ins> Answer: </ins> <br> <br>
As a wildlife conservationist in India, I can identify several key issues and threats to wildlife conservation in the country. Some of the major concerns include:

1. Habitat loss and fragmentation due to deforestation, urbanization, and infrastructure development.
2. Poaching and trafficking of endangered species, including tigers, elephants, and rhinos.
3. Climate change, which is altering ecosystems and disrupting the delicate balance of nature.
4. Human-wildlife conflict, where crops, livestock, and human settlements encroach on wildlife habitats.
5. Inadequate laws and enforcement mechanisms, making it difficult to protect endangered species and prevent wildlife crimes.
6. Lack of community engagement and awareness about wildlife conservation, leading to a lack of support for conservation efforts.
7. Pollution, including air, water, and soil pollution, which can harm wildlife and ecosystems.
8. Over-exploitation of natural resources, such as timber, minerals, and fossil fuels, which can lead to habitat destruction.

Some specific examples of threatened species in India include:

* The Asiatic lion, which is critically endangered due to habitat loss and human-wildlife conflict.
* The Bengal tiger, which is endangered due to poaching, habitat loss, and human-tiger conflict.
* The Asian elephant, which is vulnerable due to habitat loss, poaching, and human-elephant conflict.

Overall, addressing these issues will require a coordinated effort from governments, local communities, conservation organizations, and individuals to protect India's rich biodiversity and ensure the long-term survival of its wildlife populations.

<ins> Question: </ins> <br> <br>
What is the publication by brittani?

<ins> Answer: </ins> <br> <br>
According to the text, Brittani Sponaugle published an article titled "The Importance of Wildlife: Human Survival Depends on It" in May 2014.

<ins> Question: </ins> <br> <br>
Pls provide graphical statistics of tiger population in india over the last decade?

<ins> Answer: </ins> <br> <br>
I'd be happy to help you with that. As a wildlife conservation scientist in India, I have access to reliable data and can provide you with some graphical statistics on the tiger population in India over the last decade.

However, please note that the most accurate and up-to-date information on tiger populations in India is provided by the Indian Board of Wildlife (IBW) and the National Tiger Conservation Authority (NTCA). According to their latest reports, here are some key statistics:

1. **Tiger Population Trend:** According to the NTCA's annual reports, the estimated tiger population in India has shown a decline from 2014 to 2020.

2. **State-wise Breakdown:**

 * 2014: Total 2,226 tigers
 * 2020: Total 2,967 tigers

3. **Year-over-Year Change:**

 | Year | Estimated Tiger Population |
 | --- | --- |
 | 2014 | 2,226 |
 | 2015 | 2,264 (1.5% increase) |
 | 2016 | 2,000 (11.9% decrease) |
 | 2017 | 2,067 (3.35% increase) |
 | 2018 | 2,071 (0.4% increase) |
 | 2019 | 2,234 (6.8% increase) |
 | 2020 | 2,967 (33.2% increase from 2019) |

4. **Geographical Distribution:**

 * As of 2020, the tiger population is distributed across 17 states in India.
 | State | Estimated Tiger Population (2020) |
 | --- | --- |
 | Madhya Pradesh | 131 |
 | Maharashtra | 106 |
 | Karnataka | 102 |
 | Tamil Nadu | 62 |
 | Kerala | 43 |

5. **Habitat Loss and Human-Tiger Conflict:**

 * Habitat loss and fragmentation are the main threats to tiger conservation in India.
 * Human-tiger conflict has also been on the rise, with increasing human settlements and agricultural activities encroaching into tiger habitats.

Please note that these statistics might not reflect the exact numbers due to varying methodologies used by different organizations. However, they provide a general idea of the trend and changes observed over the last decade.
