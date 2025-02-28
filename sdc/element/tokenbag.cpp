#include <iostream>
#include <vector>
#include <unordered_map>
#include <random>
#include <algorithm>
#include <string>
#include "token.cpp"  // 假设 Token 和 GemType 类已经定义在 token.cpp 文件中

class TokenBag {
private:
    std::vector<Token> tokens;  // 存储所有卡牌的容器

public:
    // 构造函数，初始化 TokenBag
    TokenBag() {
        // 初始化 GemType 的数量
        std::unordered_map<GemType, int> gem_type_counts = {
            {GemType::BLACK, 4},
            {GemType::BLUE, 4},
            {GemType::GREEN, 4},
            {GemType::RED, 4},
            {GemType::WHITE, 4},
            {GemType::PEARL, 2},
            {GemType::GOLD, 3}
        };

        // 根据 gem_type_counts 创建卡牌
        for (const auto& pair : gem_type_counts) {
            for (int i = 0; i < pair.second; ++i) {
                tokens.push_back(Token(pair.first));  // 添加对应的 Token
            }
        }

        shuffle();  // 打乱卡牌
    }

    // 打乱 TokenBag 中的卡牌
    void shuffle() {
        std::random_device rd;
        std::mt19937 g(rd());  // Mersenne Twister 引擎
        std::shuffle(tokens.begin(), tokens.end(), g);  // 打乱 tokens
    }

    // 清空 TokenBag
    void empty_bag_of_tokens() {
        tokens.clear();  // 清空卡牌容器
    }

    // 获取 TokenBag 中卡牌的数量
    int get_number_of_tokens_in_bag() const {
        return tokens.size();
    }

    // 添加卡牌到 TokenBag
    void add_tokens(const std::vector<Token>& player_tokens) {
        for (const Token& token : player_tokens) {
            tokens.push_back(token);  // 将玩家的卡牌添加到 TokenBag
        }
        shuffle();  // 打乱卡牌
    }

    // 输出 TokenBag 中所有卡牌
    void print_tokens() const {
        std::cout << "[ ";
        for (const Token& token : tokens) {
            std::cout << token << " ";  // 使用重载的 operator<< 打印每张卡牌
        }
        std::cout << "]\n";
    }

    // 重载输出流运算符，用于输出 TokenBag 对象
    friend std::ostream& operator<<(std::ostream& os, const TokenBag& bag) {
        os << "[ ";
        for (const Token& token : bag.tokens) {
            os << token << " ";  // 使用重载的 operator<< 打印每张卡牌
        }
        os << "]";
        return os;
    }
};
