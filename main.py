from core.websites_checker import check_websites_from_file


# noinspection PyBroadException
def main():
    try:
        check_websites_from_file('input.csv', delimiter=';')
    except Exception:
        print("Введенные данные имеют неверный формат. Проверьте ввод.")


if __name__ == '__main__':
    main()
