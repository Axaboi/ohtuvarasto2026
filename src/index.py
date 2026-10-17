from varasto import Varasto


def main():
    juoma1 = Varasto(100.0)
    juoma2 = Varasto(100.0, 20.2)

    juoma1.lisaa_varastoon(50.7)
    juoma1.ota_varastosta(3.14)


    huono = Varasto(100.0, -50.7)
    print(huono)

    juoma2.lisaa_varastoon(1000.0)

    juoma1.lisaa_varastoon(-666.0)


if __name__ == "__main__":
    main()
