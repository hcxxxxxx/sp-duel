#include <iostream>
#include <string>

// 定义 GemType 枚举
enum class GemType {
    BLUE = 1,
    WHITE,
    GREEN,
    BLACK,
    RED,
    PEARL,
    GOLD,
    ANY
};

// 重载 GemType 枚举的输出
std::ostream& operator<<(std::ostream& os, GemType gem) {
    switch (gem) {
        case GemType::BLUE:
            os << "blue";
            break;
        case GemType::WHITE:
            os << "white";
            break;
        case GemType::GREEN:
            os << "green";
            break;
        case GemType::BLACK:
            os << "black";
            break;
        case GemType::RED:
            os << "red";
            break;
        case GemType::PEARL:
            os << "pearl";
            break;
        case GemType::GOLD:
            os << "gold";
            break;
        case GemType::ANY:
            os << "any";
            break;
    }
    return os;
}

// 定义 Token 类
class Token {
public:
    GemType gem_type;  // 使用 GemType 枚举
    std::string image;  // 存储图片路径

    // 构造函数
    Token(GemType gem_type = GemType::ANY) {
        this->gem_type = gem_type;
        this->image = "images/" + gemToString(gem_type) + ".jpeg";  // 设置图片路径
    }

    // 转换 GemType 枚举为字符串
    std::string gemToString(GemType gem_type) {
        switch (gem_type) {
            case GemType::BLUE:
                return "blue";
            case GemType::WHITE:
                return "white";
            case GemType::GREEN:
                return "green";
            case GemType::BLACK:
                return "black";
            case GemType::RED:
                return "red";
            case GemType::PEARL:
                return "pearl";
            case GemType::GOLD:
                return "gold";
            case GemType::ANY:
                return "any";
            default:
                return "";
        }
    }

    // 打印 Token 的信息
    void printToken() const {
        std::cout << "Gem Type: " << gem_type << ", Image: " << image << std::endl;
    }

    // 重载输出流运算符，用于输出 Token 对象
    friend std::ostream& operator<<(std::ostream& os, const Token& token) {
        os << token.gem_type;
        return os;
    }
};
