import logging
from telegram import Update
from sgc import programar_servico
from telegram.ext import (
    filters,
    MessageHandler,
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
from sgc import main_sgc
import datetime
import pytz


class app:
    def __init__(self, token) -> None:
        self.now = datetime.datetime.now(pytz.timezone("UTC"))
        self.chave = "t200521"
        self.senha = "marcelo1"
        self.impressora = "pdpgo125"
        self.token = token
        application = ApplicationBuilder().token(self.token).build()

        start_handler = CommandHandler("start", self.start)
        application.add_handler(start_handler)

        tela_21_handler = CommandHandler("21", self.tela21)
        application.add_handler(tela_21_handler)

        tela_21_programar_handler = CommandHandler(
            "21_programar", self.tela21_programar
        )
        application.add_handler(tela_21_programar_handler)

        tela_21_handler = CommandHandler("32", self.programar_p_equipe)
        application.add_handler(tela_21_handler)

        tela_21_handler = CommandHandler("58", self.imprimir_ase)
        application.add_handler(tela_21_handler)

        unknown_handler = MessageHandler(filters.COMMAND, self.unknown)
        application.add_handler(unknown_handler)

        application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo)
        )

        application.run_polling()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Bot desenvolvido por Marcelo Santos para programação de serviços Sanepar\n\
        Envie /comandos para ver a lista de comandos ou clique no botão no canto inferior esquerdo.",
        )

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.message.text == "tset":
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text="Test"
            )

    async def tela21(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Verificando tela 21, aguarde."
        )
        main_sgc.sgc(chave="t200521", senha="marcelo1", impressora="pdpgo125")
        self.dados, self.index = main_sgc.verificar_tela_21_emergencial()
        if len(self.dados) == 0:
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text="Sem protocolos pendentes"
            )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Protocolos atuais na tela 21 emergencial",
            )
        for i in range(0, len(self.dados), 6):
            corpo = f"\
COD: {self.dados[i]}\n\
Protocolo: {self.dados[i+1][:8]}.{self.dados[i+1][8:12]}.{self.dados[i+1][12:]}\n\
Equipe: {self.dados[i+2]}\n\
Local: {self.dados[i+3]}\n\
Endereço: {self.dados[i+4]}\n\
Motivo: {self.dados[i+5]}"
            await context.bot.send_message(chat_id=update.effective_chat.id, text=corpo)

    async def tela21_programar(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Qual a equipe para troca de hidrometros?",
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Qual a equipe para troca de hidrometros?",
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Verificando tela 21, aguarde."
        )
        main_sgc.sgc(chave="<chave>", senha="<senha>", impressora="<impressora>")
        self.dados, self.index = main_sgc.verificar_tela_21_programado()
        if len(self.dados) == 0:
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text="Sem protocolos pendentes"
            )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Protocolos atuais na tela 21 emergencial",
            )
        for i in range(0, len(self.dados), 6):
            corpo = f"\
COD: {self.dados[i]}\n\
Protocolo: {self.dados[i+1][:8]}.{self.dados[i+1][8:12]}.{self.dados[i+1][12:]}\n\
Equipe: {self.dados[i+2]}\n\
Local: {self.dados[i+3]}\n\
Endereço: {self.dados[i+4]}\n\
Motivo: {self.dados[i+5]}"
            await context.bot.send_message(chat_id=update.effective_chat.id, text=corpo)

    async def imprimir_ase(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        mensagem_pai = update.effective_message.reply_to_message.text
        protocolo = mensagem_pai[21:29] + mensagem_pai[30:34] + mensagem_pai[35:41]
        main_sgc.imprimir_servico(protocolo=protocolo)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Ase enviado para a impressora {self.impressora}",
        )

    async def programar_p_equipe(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        equipe = update.message.text
        equipe = equipe[4:]
        mensagem_pai = update.effective_message.reply_to_message.text
        protocolo = mensagem_pai[21:29] + mensagem_pai[30:34] + mensagem_pai[35:41]
        main_sgc.programar_servico_emergencial(protocolo=protocolo, equipe=equipe)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=protocolo)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=equipe)

    async def caps(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text_caps = " ".join(context.args).upper()
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

    async def unknown(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Sorry, I didn't understand that command.",
        )


TOKEN = "<TOKEN>"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


if __name__ == "__main__":
    app = app(token=TOKEN)
