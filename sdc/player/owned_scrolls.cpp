#include <SFML/Graphics.hpp>
#include <iostream>

class OwnedScrolls {
private:
    int scrolls = 0;  // 卷轴的数量
    sf::Font font;

public:
    OwnedScrolls(sf::Font& font) : font(font) {
        scrolls = 0;
    }

    void takeScroll() {
        scrolls += 1;  // 增加卷轴
    }

    void useScroll() {
        if (scrolls > 0) {
            scrolls -= 1;  // 使用卷轴
        }
    }

    int getScrolls() const {
        return scrolls;  // 获取卷轴数量
    }
};
