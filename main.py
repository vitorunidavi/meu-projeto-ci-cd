import logging
import sys

# Configuração básica do logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def greet_user(name: str) -> str:
    """
    Retorna uma mensagem de boas-vindas personalizada.
    
    Args:
        name (str): Nome do usuário.
    
    Returns:
        str: Mensagem de boas-vindas.
    """
    if not name:
        raise ValueError("O nome não pode estar vazio.")
    return f"Olá, {name}! Bem-vindo ao mundo do CI/CD."

def main():
    """
    Função principal que interage com o usuário e exibe uma mensagem.
    """
    try:
        # Solicita o nome do usuário
        user_name = input("Por favor, digite seu nome: ").strip()
        
        # Exibe a mensagem de boas-vindas
        greeting = greet_user(user_name)
        print(greeting)
        
        # Log da mensagem
        logging.info(f"Mensagem exibida para o usuário: {user_name}")
    
    except ValueError as e:
        logging.error(f"Erro: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
