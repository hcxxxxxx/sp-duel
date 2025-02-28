#include <iostream>
#include <string>

// 定义 SpecialEffect 枚举
enum class SpecialEffect {
    PLAY_AGAIN = 1,
    TAKE_SAME_COLOR = 2,
    TAKE_SCROLL = 3,
    TAKE_OPPONENT_TOKEN = 4
};

// 重载 SpecialEffect 枚举的输出
std::ostream& operator<<(std::ostream& os, SpecialEffect effect) {
    switch (effect) {
        case SpecialEffect::PLAY_AGAIN:
            os << "PLAY_AGAIN";
            break;
        case SpecialEffect::TAKE_SAME_COLOR:
            os << "TAKE_SAME_COLOR";
            break;
        case SpecialEffect::TAKE_SCROLL:
            os << "TAKE_SCROLL";
            break;
        case SpecialEffect::TAKE_OPPONENT_TOKEN:
            os << "TAKE_OPPONENT_TOKEN";
            break;
    }
    return os;
}

// 定义 Card 类
class Card {
public:
    // 成员变量
    int card_id = 0;
    int level = 0;
    int cost = 0;
    int value = 0;
    std::string color;
    int crowns = 0;
    int victory_points = 0;
    SpecialEffect special_effect;

    // 构造函数
    Card(int card_id = 0, int level = 0, int cost = 0, int value = 0, std::string color = "", int crowns = 0,
         int victory_points = 0, SpecialEffect special_effect = SpecialEffect::PLAY_AGAIN)
        : card_id(card_id), level(level), cost(cost), value(value), color(color), crowns(crowns),
          victory_points(victory_points), special_effect(special_effect) {}

    // 输出函数，用于打印卡牌信息
    void printCard() const {
        std::cout << "Card ID: " << card_id << ", Level: " << level << ", Cost: " << cost << ", Value: " << value
                  << ", Color: " << color << ", Crowns: " << crowns << ", Victory Points: " << victory_points
                  << ", Special Effect: " << special_effect << std::endl;
    }

    // 重载输出运算符，以便输出卡牌的 ID
    friend std::ostream& operator<<(std::ostream& os, const Card& card) {
        os << card.card_id;
        return os;
    }
};