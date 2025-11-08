from proto.compiled import interaction_pb2
import time
from google.protobuf.json_format import MessageToJson


## Example of a normal transaction
transaction = interaction_pb2.Transaction()

transaction.datetime.seconds = int(time.time())
transaction.transactee_1.name = 'transactor1'
transaction.transactee_1.type = interaction_pb2.TransactionalEntity.TRANSACTEE
transaction.transactee_2.name = 'transactor2'
transaction.transactee_2.type = interaction_pb2.TransactionalEntity.TRANSACTEE

transaction.transactee_2_given.description = 'GBP'
transaction.transactee_2_given.physical_quantity.dimension = 'cur'
transaction.transactee_2_given.physical_quantity.value = 2

transaction.transactee_1_given.description = 'flour'
transaction.transactee_1_given.physical_quantity.dimension = 'kg'
transaction.transactee_1_given.physical_quantity.value = 2

print(transaction)

## Example of a generative transaction
generative_transaction = interaction_pb2.Transaction()
generative_transaction.CopyFrom(transaction)
generative_transaction.consumed_resource.description = 'energy'
generative_transaction.consumed_resource.physical_quantity.value = 10
generative_transaction.consumed_resource.physical_quantity.dimension = 'J'
generative_transaction.generated_resource.description = 'energy'
generative_transaction.generated_resource.physical_quantity.value = 10
generative_transaction.generated_resource.physical_quantity.dimension = 'J'

print(generative_transaction)

transaction_history = interaction_pb2.TransactionHistory()
unqual_transaction = transaction_history.transactions.add()
unqual_transaction.CopyFrom(transaction)
unqual_transaction2 = transaction_history.transactions.add()
unqual_transaction2.CopyFrom(generative_transaction)


def resource_to_string(resource):
    string = '[{} {} {}]'.format(resource.physical_quantity.dimension,
                               resource.description,
                               resource.physical_quantity.value
                               )
    return string
def transaction_to_string(transaction):
    string = '{} <> {};  {} == {} | {} || '.format( transaction.transactee_1.name,
                                  transaction.transactee_2.name,
                                  resource_to_string(transaction.transactee_1_given),
                                  resource_to_string(transaction.transactee_2_given),
                                  transaction.datetime.seconds)
    string += resource_to_string(transaction.generated_resource) + '^ |'
    string += resource_to_string(transaction.consumed_resource) + 'v'
    return(string)

print(transaction_to_string(transaction))
print(transaction_to_string(generative_transaction))

transaction_mol= interaction_pb2.Transaction()

transaction_mol.datetime.seconds = int(time.time())
transaction_mol.transactee_1.name = 'molecule1'
transaction_mol.transactee_1.type = interaction_pb2.TransactionalEntity.TRANSACTEE
transaction_mol.transactee_2.name = 'molecule2'
transaction_mol.transactee_2.type = interaction_pb2.TransactionalEntity.TRANSACTEE

transaction_mol.transactee_2_given.description = 'phosphate ion'
transaction_mol.transactee_2_given.physical_quantity.dimension = '[count]'
transaction_mol.transactee_2_given.physical_quantity.value = 1

transaction_mol.transactee_1_given.description = 'phosphate ion'
transaction_mol.transactee_1_given.physical_quantity.dimension = '[count]'
transaction_mol.transactee_1_given.physical_quantity.value = -1

print(transaction_to_string(transaction_mol))
