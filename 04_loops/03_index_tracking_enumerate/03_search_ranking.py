"""
Search Result Ranking.
"""

from typing import List, Dict, Any

def rank_search_results(results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Adds ranking to search results.
    
    Args:
        results: List of search result dictionaries
    
    Returns:
        Results with ranking added
    
    Real-world use case: Search engines, recommendation systems.
    """
    ranked_results = []
    
    for rank, result in enumerate(results, start=1):
        result_with_rank = result.copy()
        result_with_rank["rank"] = rank
        ranked_results.append(result_with_rank)
    
    return ranked_results


def demonstrate_ranking() -> None:
    """
    Demonstrates search result ranking.
    """
    search_results = [
        {"title": "Python Tutorial", "score": 0.95},
        {"title": "Python Documentation", "score": 0.89},
        {"title": "Learn Python", "score": 0.82},
    ]
    
    ranked = rank_search_results(search_results)
    print("\nRanked search results:")
    for result in ranked:
        print(f"  #{result['rank']}: {result['title']} (Score: {result['score']})")


if __name__ == "__main__":
    demonstrate_ranking()
