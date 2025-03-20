import streamlit as st
import os

def add_contact (list):
    contact_name = input("Nome do contato: ")
    contact_phone = input("Telefone do contato: ")
    contact_mail = input("Email do contato: ")

    new_contact = {"nome": contact_name, "telefone": contact_phone, "email": contact_mail, "favorite": False}
    list.append(new_contact)

    print(f"Contato '{contact_name}' adicionado com sucesso!")
    return

def view_contact (list):
    print("Lista de contatos:")
    for index, contact in enumerate(list, start=1):
        status = "❤︎" if contact["favorite"] else " "
        contact_name = contact["nome"]
        contact_phone = contact["telefone"]
        contact_mail = contact["email"]

        print("----------------------------------------")
        print(f"{index}. Nome: {contact_name} {status}")
        print(f"   Telefone: {contact_phone}")
        print(f"   Email: {contact_mail}")
        print("----------------------------------------")
                
    return

def edit_contact (list, index):
    adjusted_index = index - 1
    contact_name = list[adjusted_index]["nome"]
    contact_phone = list[adjusted_index]["telefone"]
    contact_mail = list[adjusted_index]["email"]

    print(f"""
            O que deseja mudar?
            1- Nome: {contact_name}
            2- Telefone: {contact_phone}
            3- Email: {contact_mail}
    """)

    choice = int(input("O que deseja alterar: "))

    if choice == 1:
        contact_name = input("Insira o novo nome: ")
        list[adjusted_index]["nome"] = contact_name

    elif choice == 2:
        contact_phone = input("Insira o novo telefone: ")
        list[adjusted_index]["telefone"] = contact_phone

    elif choice == 3:
        contact_mail = input("Insira o novo email: ")
        list[adjusted_index]["email"] = contact_mail

    else:
        print("Dado não encontrado!")

    print("Dado alterado com sucesso!")
    return

def favorite_contact(list, index):
    adjusted_index = int(index) - 1
    
    if list[adjusted_index]["favorite"] == False: 
        list[adjusted_index]["favorite"] = True
        print(f"Contato {index} marcado como favorito!")
    else:
        list[adjusted_index]["favorite"] = False
        print(f"Contato {index} desfavoritado!")

    return

def view_favorites(list):
    print("Lista de favoritos:")
    for index, contact in enumerate(list, start=1):

        contact_name = contact["nome"]

        if contact["favorite"] == True:
            print("----------------------------------------")
            print(f"{index}. Nome: {contact_name} ❤︎")
            print("----------------------------------------")

    return

def delete_contact(list, index):
    adjusted_index = index - 1
    contact_name = list[adjusted_index]["nome"]

    if list[adjusted_index]:
        list.remove(list[adjusted_index])

    print(f"Contato {index}. {contact_name} removido com sucesso!")
    
    return

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear") # clears terminal after each repetition
    return

contacts_list = []

while True:
    print(
        """
        -------------- AGENDA DE CONTATOS -----------------
        (1) - Adicionar contato.
        (2) - Visualizar contatos.
        (3) - Editar contato.
        (4) - Marcar/Desmarcar contato como favorito.
        (5) - Ver favoritos.
        (6) - Apagar contato.
        (7) - Sair 
        """
    )

    choice = input("Digite sua escolha: ")

    match choice:
        case "1":
            clear_terminal()
            add_contact(contacts_list)

        case "2":
            clear_terminal()
            view_contact(contacts_list)

        case "3":
            clear_terminal()
            view_contact(contacts_list)
            contact_index = int(input("Digite o numero do contato que deseja alterar: "))
            edit_contact(contacts_list, contact_index)
        
        case "4":
            clear_terminal()
            view_contact(contacts_list)
            contact_index = input("Digite qual contato quer favoritar/desfavoritar: ")
            favorite_contact(contacts_list, contact_index)

        case "5":
            clear_terminal()
            view_favorites(contacts_list)

        case "6":
            clear_terminal()
            view_contact(contacts_list)
            contact_index = int(input("Digite qual contato deseja excluir: "))
            delete_contact(contacts_list, contact_index)

        case "7":
            break