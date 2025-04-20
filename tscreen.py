# type: ignore
import customtkinter as ctk


def screen():
    ctk.set_appearance_mode('dark')

    app = ctk.CTk()
    app.title('Movimento de Caixa')
    app.geometry('800x800')

    # Variáveis para armazenar os valores dos campos
    documento = ctk.StringVar()
    historico = ctk.StringVar()
    entrada = ctk.StringVar()
    saida = ctk.StringVar()
    linha_adicional = ctk.StringVar()

    # Widgets da interface
    ad = ctk.CTkLabel(
        app, text='Ao fechar a janela do programa, o arquivo excel criado será movido para a pasta "Tables" na área de trabalho!'
    )
    ad.pack(pady=10)

    ad2 = ctk.CTkLabel(
        app, text='Ao optar por linhas adicionais, os campos para dados serão limpos e você poderá inserir novos dados!'
    )
    ad2.pack(pady=10)

    num = ctk.CTkLabel(app, text='Número do documento')
    num.pack(pady=10)

    num_e = ctk.CTkEntry(
        app, placeholder_text='Digite o n° do doc:', textvariable=documento
        )
    num_e.pack(pady=10)

    abt = ctk.CTkLabel(app, text='Histórico')
    abt.pack(pady=10)

    abt_e = ctk.CTkEntry(
        app, placeholder_text='Digite o histórico:', textvariable=historico
        )
    abt_e.pack(pady=10)

    ente = ctk.CTkLabel(app, text='Entrada')
    ente.pack(pady=10)

    ente_e = ctk.CTkEntry(
        app, placeholder_text='Digite a entrada:', textvariable=entrada
        )
    ente_e.pack(pady=10)

    exy = ctk.CTkLabel(app, text='Saída')
    exy.pack(pady=10)

    exy_e = ctk.CTkEntry(
        app, placeholder_text='Digite a saída:', textvariable=saida
        )
    exy_e.pack(pady=10)

    lin = ctk.CTkLabel(app, text='Linha adicional (s/n)')
    lin.pack(pady=10)

    lin_e = ctk.CTkEntry(
        app, placeholder_text='(s/n):', textvariable=linha_adicional
        )
    lin_e.pack(pady=10)

    # Frame para mensagens
    message_frame = ctk.CTkFrame(app)
    message_frame.pack(pady=10)
    message_label = ctk.CTkLabel(message_frame, text="")
    message_label.pack()

    def movimento_caixa():
        try:
            doc_value = documento.get()
            hist_value = historico.get()
            ent_value = entrada.get()
            sai_value = saida.get()
            lin_value = linha_adicional.get().lower()

            if not all([doc_value, hist_value]):
                message_label.configure(
                    text="Preencha todos os campos obrigatórios!"
                    )
                return

            from sheet import create
            create(doc_value, hist_value, ent_value, sai_value)

            if lin_value == 's':
                documento.set("")
                historico.set("")
                entrada.set("")
                saida.set("")
                linha_adicional.set("")
                message_label.configure(
                    text="Campos limpos! Insira novos dados."
                    )
            else:
                message_label.configure(text="Movimento de Caixa Registrado.")

        except ImportError:
            message_label.configure(
                text="Erro: Não foi possível importar a função create"
                )
        except Exception as e:
            message_label.configure(text=f"Erro: {str(e)}")

    ctk.CTkButton(
        app, text='Movimento de Caixa', command=movimento_caixa
        ).pack(pady=30)

    app.mainloop()
