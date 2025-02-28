#include <SFML/Graphics.hpp>
#include <iostream>
#include <map>
#include <vector>

enum class GemType {
    RED, GREEN, BLUE, BLACK, WHITE, PEARL, GOLD, ANY
};

// 获取 GemType 的字符串表示
std::string gemTypeToString(GemType gem) {
    switch (gem) {
        case GemType::RED: return "RED";
        case GemType::GREEN: return "GREEN";
        case GemType::BLUE: return "BLUE";
        case GemType::BLACK: return "BLACK";
        case GemType::WHITE: return "WHITE";
        case GemType::PEARL: return "PEARL";
        case GemType::GOLD: return "GOLD";
        default: return "ANY";
    }
}

class OwnedTokens {
private:
    std::map<GemType, int> tokens;  // 存储每种颜色的代币数量
    std::map<GemType, sf::Text> tokenWidgets;  // 用于显示代币数量的文本
    sf::Font font;  // 用于渲染文本的字体

public:
    OwnedTokens(sf::Font& font) : font(font) {
        // 初始化代币数量
        tokens[GemType::RED] = 0;
        tokens[GemType::GREEN] = 0;
        tokens[GemType::BLUE] = 0;
        tokens[GemType::BLACK] = 0;
        tokens[GemType::WHITE] = 0;
        tokens[GemType::PEARL] = 0;
        tokens[GemType::GOLD] = 0;

    }

    void draw(sf::RenderWindow& window) {
        // 绘制所有的代币数量
        for (const auto& entry : tokenWidgets) {
            window.draw(entry.second);
        }
    }

    void addTokens(const std::vector<GemType>& tokensList) {
        // 增加代币数量
        for (GemType token : tokensList) {
            tokens[token]++;
        }
    }

    void removeTokens(const std::map<GemType, int>& tokensToPay) {
        // 移除指定颜色的代币
        for (const auto& entry : tokensToPay) {
            GemType color = entry.first;
            int amountToPay = entry.second;
            if (tokens[color] < amountToPay) {
                tokens[GemType::GOLD] -= (amountToPay - tokens[color]);
                tokens[color] = 0;
            } else {
                tokens[color] -= amountToPay;
            }
        }
    }

    void takeToken(GemType color) {
        if (tokens[color] > 0) {
            tokens[color]--;
        }
    }

    void addToken(GemType color) {
        tokens[color]++;
    }
};
