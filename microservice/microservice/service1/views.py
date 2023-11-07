from django.shortcuts import render, HttpResponse
from service1 import models
from opentelemetry import trace
# from opentelemetry.exporter.jaeger.thrift import JaegerExporter
# from opentelemetry.instrumentation.django import DjangoInstrumentor
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import BatchSpanProcessor
# from opentelemetry.sdk.resources import SERVICE_NAME, Resource
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import (
#     BatchSpanProcessor,
#     ConsoleSpanExporter,
# )
# import os

# Create your views here.

# provider = TracerProvider()
# processor = BatchSpanProcessor(ConsoleSpanExporter())
# provider.add_span_processor(processor)

# trace.set_tracer_provider(provider)
# tracer = trace.get_tracer(__name__)

# jaeger_exporter = JaegerExporter(
#     agent_host_name=os.getenv("TRACING_HOST"),
#     agent_port= int(os.getenv("TRACING_PORT")),
# )

# trace.set_tracer_provider(TracerProvider(
#     resource=Resource.create({SERVICE_NAME: 'service1'})
# ))

# span_processor = BatchSpanProcessor(jaeger_exporter)

# trace.get_tracer_provider().add_span_processor(span_processor)

tracer = trace.get_tracer(__name__)

def index(request):
    return HttpResponse('Hello, World!  —— from service1')

def begin(request):
    return HttpResponse('Welcome to Microservice Homepage')

def get_number():
    with tracer.start_as_current_span("span-name") as span:
        i = models.book.objects.filter(name='水浒传').values('id')
        return i