import os
import time
# deleted > from MainScores import score_server

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 500


def screen_cleaner():
    time.sleep(1.0)
    os.system('cls')


def score_insert_to_file(actual_score):
    try:
        scores_file_name = open(SCORES_FILE_NAME, 'r+')
        read_score_file = int(scores_file_name.read())
        scores_file_name.seek(0)
        final_score = read_score_file+actual_score
        scores_file_name.write(f'{final_score}')
        scores_file_name.truncate()
        print(f"Your Score is {final_score}")
        scores_file_name.close()
        # deleted > score_server(final_score)
        return final_score

    except Exception:
        scores_file_name = open(SCORES_FILE_NAME, 'w+')
        # scores_file_name.seek(0)
        scores_file_name.write(f'{actual_score}')
        scores_file_name = open(SCORES_FILE_NAME, 'r+')
        read_score_file = scores_file_name.read()
        print(f"Your Score is {read_score_file}")
        # scores_file_name.truncate()
        scores_file_name.close()