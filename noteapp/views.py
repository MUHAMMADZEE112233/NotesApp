import os
import textwrap

from langchain.document_loaders import Docx2txtLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate

from .serializers import NotesSerializer
from .models import Notess

os.environ['OPENAI_API_KEY']= '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'


class NoteListAPI(generics.ListCreateAPIView):
    queryset = Notess.objects.all()
    serializer_class = NotesSerializer


class NoteDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notess.objects.all()
    serializer_class = NotesSerializer


class SummarizeTextView(APIView):
    def get(self, request, notes_id, *args, **kwargs):
        try:
            input_text = NotesSerializer(Notess.objects.get(id=notes_id)).data['content']
            if input_text:
                # Define prompt
                # doc = Document(page_content=input_text, metadata={"source": "local"})

                prompt_template = """Write a concise summary of the following:
                "{text}"
                CONCISE SUMMARY:"""
                prompt_template = PromptTemplate(template=prompt_template,
                                                 input_variables=["text"])

                # Define the LLM
                llm_key = os.environ.get("OPENAI_API_KEY")
                llm = OpenAI(api_key=llm_key, temperature=0)

                # Generating the document summary
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt_template)
                text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
                pages = text_splitter.split_text(input_text)

                text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
                input_text = text_splitter.create_documents(pages)

                summarized_text = chain.run(input_text)
                summarized_text = textwrap.fill(summarized_text,
                                                width=100,
                                                break_long_words=False,
                                                replace_whitespace=False)

                return Response({"summarized_text": summarized_text}, status=status.HTTP_200_OK)
            return Response(f"This Note ID: {notes_id} does not have any content!!!", status=200)
        except Exception as e:
            return Response(str(e), status=500)
