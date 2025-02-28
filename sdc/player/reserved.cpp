#include <SFML/Graphics.hpp>
#include "../element/card.cpp"
#include <iostream>
#include <vector>
#include <string>

class Reserved {
private:
    std::vector<Card> reserved_cards;  // 存储保留的卡片

public:
    Reserved(std::vector<Card> reserved_cards)
        : reserved_cards(reserved_cards) {
    }

    void updateReservedCardsDisplay() {
    }

    void draw(sf::RenderWindow& window) {
    }

    Card buyCard(int index) {
        if (index >= 0 && index < reserved_cards.size()) {
            Card cardBought = reserved_cards[index];
            reserved_cards.erase(reserved_cards.begin() + index);  // 移除该卡片
            updateReservedCardsDisplay();
            return cardBought;
        }
        return {};  // 如果索引无效，返回一个空卡片
    }

    void reserveCard(const Card& card) {
        reserved_cards.push_back(card);
        updateReservedCardsDisplay();
    }

    const std::vector<Card>& getReservedCards() const {
        return reserved_cards;
    }
};

