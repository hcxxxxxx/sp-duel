#include <SFML/Graphics.hpp>
#include "owned_tokens.cpp"
#include "owned_scrolls.cpp"
#include "owned_cards.cpp"
#include "../element/card.cpp"
#include <iostream>
#include <map>
#include <vector>

class Reserved {
private:
    std::vector<Card> reservedCards;
};

class Player {
private:
    std::string name;
    OwnedTokens ownedTokens;
    OwnedScrolls ownedScrolls;
    OwnedCardBox ownedCards;
    Reserved reservedCards;

public:
    Player(const std::string& name, std::vector<Card> reserved, sf::Font& font)
        : name(name), ownedTokens(font), ownedScrolls(font), ownedCards(font), reservedCards({}) {}

    std::string getName() const {
        return name;
    }
};

