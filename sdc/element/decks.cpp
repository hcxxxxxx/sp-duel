#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

class Deck {
private:
    std::vector<int> cards;  // 使用 vector 来存储卡牌

public:
    // 构造函数，接受一个初始的卡牌列表
    Deck(const std::vector<int>& db_cards = {}) {
        cards = db_cards;  // 将传入的卡牌拷贝到 cards 中
        shuffle();  // 打乱卡牌
    }

    // 打乱卡牌的函数
    void shuffle() {
        std::random_device rd;
        std::mt19937 g(rd());  // 使用 Mersenne Twister 引擎
        std::shuffle(cards.begin(), cards.end(), g);  // 打乱卡牌
    }

    // 抽取一张卡牌
    int draw_card() {
        if (!cards.empty()) {
            int card = cards.back();  // 取出最后一张卡牌
            cards.pop_back();  // 从容器中移除这张卡牌
            return card;
        }
        return -1;  // 如果卡牌空了，返回 -1 作为表示
    }

    // 重载输出流运算符，以便打印卡牌
    friend std::ostream& operator<<(std::ostream& os, const Deck& deck) {
        os << "[";
        for (size_t i = 0; i < deck.cards.size(); ++i) {
            os << deck.cards[i];
            if (i != deck.cards.size() - 1) os << ", ";
        }
        os << "]";
        return os;
    }
};
