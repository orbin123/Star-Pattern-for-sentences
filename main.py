def print_star_pattern(letter):
    patterns = {
        'A': ["   *   ", "  * *  ", " *   * ", "*******", "*     *", "*     *"],
        'B': ["****** ", "*     *", "*     *", "****** ", "*     *", "****** "],
        'C': [" ***** ", "*     *", "*      ", "*      ", "*     *", " ***** "],
        'D': ["****** ", "*     *", "*     *", "*     *", "*     *", "****** "],
        'E': ["*******", "*      ", "*      ", "****** ", "*      ", "*******"],
        'F': ["*******", "*      ", "*      ", "****** ", "*      ", "*      "],
        'G': [" ***** ", "*      ", "*  ****", "*     *", "*     *", " ***** "],
        'H': ["*     *", "*     *", "*******", "*     *", "*     *", "*     *"],
        'I': ["*******", "   *   ", "   *   ", "   *   ", "   *   ", "*******"],
        'J': ["  *****", "     * ", "     * ", "     * ", "*    * ", " ****  "],
        'K': ["*    * ", "*   *  ", "*  *   ", "***    ", "*  *   ", "*   *  "],
        'L': ["*      ", "*      ", "*      ", "*      ", "*      ", "*******"],
        'M': ["*     *", "**   **", "* * * *", "*  *  *", "*     *", "*     *"],
        'N': ["*     *", "**    *", "* *   *", "*  *  *", "*   * *", "*    **"],
        'O': [" ***** ", "*     *", "*     *", "*     *", "*     *", " ***** "],
        'P': ["****** ", "*     *", "*     *", "****** ", "*      ", "*      "],
        'Q': [" ***** ", "*     *", "*     *", "*   * *", "*    * ", " **** *"],
        'R': ["****** ", "*     *", "*     *", "****** ", "*  *   ", "*   *  "],
        'S': [" ******", "*      ", "*      ", " ***** ", "      *", "****** "],
        'T': ["*******", "   *   ", "   *   ", "   *   ", "   *   ", "   *   "],
        'U': ["*     *", "*     *", "*     *", "*     *", "*     *", " ***** "],
        'V': ["*     *", "*     *", "*     *", " *   * ", "  * *  ", "   *   "],
        'W': ["*     *", "*     *", "*  *  *", "* * * *", "**   **", "*     *"],
        'X': ["*     *", " *   * ", "  * *  ", "   *   ", "  * *  ", " *   * "],
        'Y': ["*     *", " *   * ", "  * *  ", "   *   ", "   *   ", "   *   "],
        'Z': ["*******", "     * ", "    *  ", "   *   ", "  *    ", "*******"]
    }
    return patterns.get(letter.upper(), ["       ", "       ", "       ", "       ", "       ", "       "])

def main():
    sentence = "GET WELL SOON"
    words = sentence.split()

    for word in words:
        word_patterns = [print_star_pattern(letter) for letter in word]
        for i in range(6):
            for pattern in word_patterns:
                print(pattern[i], end="  ")
            print()
        print()

if __name__ == "__main__":
    main()
