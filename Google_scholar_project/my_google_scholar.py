

# Profile information
profile = {
    
    "name": "Evgenios Karasavvas",
    "affiliation": "Aristotle University of Thessaloniki",
    "research_interests": ["Machine Learning", "Data Science", "Python"],
}

# Papers
papers = [
    {  
        "id": 1, 
        "Title": "Energy and exergy analysis", 
        "First Author": "Evgenios Karasavvas",
        "Second Author": "Evgenios Karasavvas",
        "Third Author": "Evgenios Karasavvas",
        "Year": 2020,
        "Citations": 69
    },
    
    {
        "id": 2, 
        "Title": "Design of an integrated CSP-calcium looping", 
        "First Author": "Evgenios Karasavvas",
        "Second Author": "Evgenios Karasavvas",
        "Third Author": "Evgenios Karasavvas",
        "Year": 2020,
        "Citations": 40
     
     }
]

for paper in papers:
    print(f"Title: {paper['Title']} ==> Citations: {paper['Citations']}")
