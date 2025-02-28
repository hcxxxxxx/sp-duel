#include "../element/token.cpp"
#include <SFML/Graphics.hpp>

class OwnedCardBox {
public:
    GemType color;
    int num_tokens = 0;
    int victory_points = 0;
    int crowns = 0;
    std::vector<Token> cards;
    sf::Font font;

    OwnedCardBox(sf::Font font) : font(font){}

    void addCard(const Token& card) {
        cards.push_back(card);
        // 更新卡牌数量、点数和王冠
        num_tokens += 1;  // 简化为每增加一张卡牌增加1个token
        victory_points += 1;  // 假设每张卡牌价值1点
        crowns += 1;  // 假设每张卡牌有1个王冠
    }

    std::string gemTypeToString(GemType gem) {
        switch (gem) {
            case GemType::BLUE: return "blue";
            case GemType::WHITE: return "white";
            case GemType::GREEN: return "green";
            case GemType::BLACK: return "black";
            case GemType::RED: return "red";
            case GemType::PEARL: return "pearl";
            case GemType::GOLD: return "gold";
            case GemType::ANY: return "any";
            default: return "unknown";
        }
    }

    void updateUI() {
        // 更新 UI 显示相关数据
        std::cout << "Color: " << gemTypeToString(color) << "\n";
        std::cout << "Tokens: " << num_tokens << "\n";
        std::cout << "Victory Points: " << victory_points << "\n";
        std::cout << "Crowns: " << crowns << "\n";
    }
};
