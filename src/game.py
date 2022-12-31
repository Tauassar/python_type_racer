from src.text_generator import _get_pre_generated_paragraphs, generate_paragraphs


class GameDriver:
    paragraphs_count: int = 0

    def play(self):
        # paragraphs_count = int(input('How many paragraphs you want to have?\n'))
        #
        # print(f'Paragraph count {paragraphs_count}')
        for x in generate_paragraphs(3):
            print(x)
