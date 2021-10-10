import graphene
from graphene import relay, ObjectType, String,JSONString,Int
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Store,Invoice,Item

class StoreQL(DjangoObjectType):
    class Meta:
        model = Store
        feilds = '__all__'
class InvoiceQL(DjangoObjectType):
    class Meta:
        model = Invoice
        feilds = '__all__'
    over_all = Int()

    @staticmethod
    def resolve_over_all(root, info, **kwargs):
        return root.total_invoice()
        

class ItemQL(DjangoObjectType):
    class Meta:
        model = Item
        feilds = '__all__'
    total = Int()
    

    @staticmethod
    def resolve_total(root, info, **kwargs):
        return root.total_amount()
        
# Querying the complete database "Store", "Invoice detail", "Items-detail"

# creating the Store(POST request) creating the data from frontend
class StoreMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        email_id = graphene.String(required=True)
        address = graphene.String(required=True)
    
    store = graphene.Field(StoreQL)

    @classmethod
    def mutate(cls,root,info,name,phone_number,email_id,address):
        store = Store(name=name)
        store.name = name
        store.phone_number = phone_number
        store.email_id = email_id
        store.address = address
        store.save()
        return StoreMutation(store=store)
# Updating the store(PUT request) using the id of store
class StoreUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        phone_number = graphene.String()
        email_id = graphene.String(required=True)
    store_update = graphene.Field(StoreQL)

    @classmethod
    def mutate(cls,root,info,id,name,phone_number,email_id):
        store_update = Store.objects.get(id=id)
        store_update.name = name
        store_update.phone_number = phone_number
        store_update.email_id = email_id
        store_update.save()
        return StoreUpdateMutation(store_update=store_update)
# Deleting the store from Database using the id of sore
class StoreDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    store_delete = graphene.Field(StoreQL)

    @classmethod
    def mutate(cls,root,info,id):
        store_delete = Store.objects.get(id=id)
        store_delete.delete()
        return None








class ItemInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    quantity = graphene.Int(required=True)
    price = graphene.Int(required=True)
    discount = graphene.Float(required=True)
    gst = graphene.Int(required=True)

class InvoiceCreateMutation(graphene.Mutation):
    class Arguments:
        buyer_name = graphene.String()
        buyer_phone_number = graphene.String()
        paid = graphene.Boolean(required=True)
        items_data=ItemInput(required=True)

    invoice_create = graphene.Field(InvoiceQL)
    
    @classmethod
    def mutate(cls,root,info,buyer_name,buyer_phone_number,paid,items_data):
        items = Item.objects.create(name=items_data.name,quantity=items_data.quantity,
        price=items_data.price,discount=items_data.discount,gst=items_data.gst)
        invoice_create = Invoice(buyer_name=buyer_name,
        buyer_phone_number=buyer_phone_number,
        paid=paid,
        items=items
        )
        invoice_create.buyer_name= buyer_name
        invoice_create.buyer_phone_number= buyer_phone_number
        invoice_create.paid= paid
        invoice_create.items= items
        invoice_create.save()
        return InvoiceCreateMutation(invoice_create=invoice_create)



class Query(graphene.ObjectType):
    store = DjangoListField(StoreQL)
    invoice = DjangoListField(InvoiceQL)
    all_invoice = graphene.List(InvoiceQL,id=graphene.Int())
    all_item = graphene.Field(ItemQL, name=graphene.String(required=True))
    
    
    def resolve_all_invoice(root,info):
        return Invoice.objects.select_related("items").all()
    def resolve_all_item(root,info,name):
        try:
            return Item.objects.get(name=name)
        except Item.DoesNotExist:
            return None


class Mutation(graphene.ObjectType):
    update_store = StoreUpdateMutation.Field()
    create_store = StoreMutation.Field()
    delete_store = StoreDeleteMutation.Field()
    invoice_creation = InvoiceCreateMutation.Field()
    # item_deletion = ItemDeleteMutation.Field()





schema = graphene.Schema(query=Query,mutation=Mutation)

